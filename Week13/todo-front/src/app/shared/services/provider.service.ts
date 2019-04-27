import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {IAuthResponce, ITask, ITaskList} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }
  getTaskList(): Promise<ITaskList[]> {
    return this.get('http://localhost:8000/task_lists/', {});
  }
  getTasks(taskList: ITaskList): Promise<ITask> {
    return this.get(`http://localhost:8000/task_lists/${taskList.id}/tasks/`, {});
  }
  updateTaskList(taskList: ITaskList): Promise<ITaskList> {
    return this.put(`http://127.0.0.1:8000/task_lists/${taskList.id}/`, {
      name: taskList.name
    });
  }

  deleteTaskList(taskList: ITaskList): Promise<ITaskList> {
    return this.delet(`http://127.0.0.1:8000/task_lists/${taskList.id}/`, {});
  }

  createTaskList(taskName: any): Promise<ITaskList> {
    return this.post('http://127.0.0.1:8000/task_lists/', {
      name: taskName
    });
  }
  auth(login: any, paswd: any): Promise<IAuthResponce> {
    return this.post('http://localhost:8000/login/', {
      username: login,
      password: paswd
    });
  }
  logoutt(): Promise<any> {
    return this.post('http://localhost:8000/logout/', {});
  }
}
