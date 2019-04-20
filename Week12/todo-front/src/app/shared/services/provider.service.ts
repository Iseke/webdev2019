import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {ITask, ITaskList} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }
  getTaskList(): Promise<ITaskList[]> {
    return this.get('http://localhost:8000/api/task_lists/', {});
  }
  getTasks(taskList: ITaskList): Promise<ITask> {
    return this.get(`http://localhost:8000/api/task_lists/${taskList.id}/tasks/`, {});
  }
  deleteTask(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/task_lists/${id}/`, {});
  }
  updateTask(taskList: ITaskList): Promise<ITaskList> {
    return this.put(`http://127.0.0.1:8000/api/task_lists/${taskList.id}/`, {
      name: taskList.name
    });
  }
  createTask(nname: any): Promise<ITaskList> {
    return this.post('http://127.0.0.1:8000/api/task_lists', {
      name: nname
    });
  }
}
