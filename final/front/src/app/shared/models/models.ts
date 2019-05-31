export interface IUser {
  id: number;
  username: string;
  email: string;
}
export interface IAuth {
  token: string;
}
export interface IProduct {
  id: number;
  name: string;
  price: number;
  quantity: number;
}
export interface IUserProduct{
  id: number;
  user: IUser;
  product: IProduct;
  count: number;
}
