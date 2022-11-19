
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GetfilesService {

  constructor(private httpClient:HttpClient) { }

  getImage(imageUrl: string): Observable<Blob> {
  return this.httpClient.get(imageUrl, { responseType: 'blob' });
}
}