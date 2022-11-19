import { TestBed } from '@angular/core/testing';

import { GetfilesService } from './getfiles.service';

describe('GetfilesService', () => {
  let service: GetfilesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GetfilesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
