import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {IProduct, IUserProduct, IUser, IAuth} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }
  // @ts-ignore
  getProducts(): Promise<IProduct> {
    return this.get('http://localhost:8000/products/', {});
  }
  getUserProducts(): Promise<IUserProduct> {
    return this.get('http://localhost:8000/user_products/', {});
  }
  addProductToBasket(cnt: number, prd: IProduct): Promise<IUserProduct> {
    return this.post('http://localhost:8000/user_products/', {
      count: cnt,
      product: prd
    });
  }
  returnProductFromBasket(id: number): Promise<IUserProduct> {
    return this.delet(`http://localhost:8000/user_products/${id}`, {
    });
  }
  // @ts-ignore
  login(login: any, passwd: any): Promise<IAuth> {
    return this.post('http//localhost:8000/api/login/', {
      username: login,
      password: passwd
    });
  }
  // @ts-ignore
  logout(): Promise<any> {
    return this.post('http//localhost:8000/api/logout/', {});
  }
}
