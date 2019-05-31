import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {IUserProduct, IProduct, IUser} from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public products: IProduct;
  public userProducts: IUserProduct;
  public logged = false;
  public login: any = '';
  public password: any = '';
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token')
    if (token) {
      this.logged = true;
    }
  }
  getProducts() {
    this.provider.getProducts().then(res => {
      this.products = res;
    });
  }
  getUserProducts() {
    this.provider.getUserProducts().then(res => {
      this.userProducts = res;
    });
  }
  add(count: number, product: IProduct) {
    this.provider.addProductToBasket(count, product).then(res => {
      this.getProducts();
      this.getUserProducts();
    });
  }
  delete(id: number) {
    this.provider.returnProductFromBasket(id).then(res => {
      this.provider.getUserProducts().then( re => {
        this.userProducts = re;
      });
    });
  }
  auth() {

    if (this.login !== '' && this.password !== '') {
      this.provider.login(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.logged = true;
        // this.provider.getTaskList().then(re => {
        //   this.taskLists = re;
        // });
      });
    }
  }

  logout() {

    this.provider.logout().then(res => {
      localStorage.removeItem('token');
      this.logged = false;
    });

  }

}
