import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { AuthService } from '../_services/auth.service';
import { GetfilesService } from '../_services/getfiles.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor(private auth:AuthService,private getFile:GetfilesService) { }

  ngOnInit(): void {
    this.auth.canAccess();
  }
imageToShow: any;
  isImageLoading = false;

createImageFromBlob(image: Blob) {
   let reader = new FileReader();
   reader.addEventListener("load", () => {
      this.imageToShow = reader.result;
   }, false);

   if (image) {
      reader.readAsDataURL(image);
   }
}


  onSubmit(){
      this.isImageLoading = true;
      this.getFile.getImage("http://127.0.0.1:5000/results").subscribe({
        next:data=>{
          this.createImageFromBlob(data);
        }
      });
  }
}
