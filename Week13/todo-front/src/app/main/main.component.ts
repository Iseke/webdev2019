import {Component, OnInit} from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {ITask, ITaskList} from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  public taskLists: ITaskList[] = [];
  public tasks: ITask[] = [];
  public name: any = '';
  public logged = false;
  public login: any = '';
  public password: any = '';
  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
    const token = localStorage.getItem('token')
    if (token) {
      this.logged = true;
    }
    if (this.logged) {
      this.provider.getTaskList().then(res => {
        this.taskLists = res;
      });
    }
  }
  getTask(taskList: ITaskList) {
    this.provider.getTasks(taskList).then(res => {
      // @ts-ignore
      this.tasks = res;
    });
  }
  updateTaskList(c: ITaskList) {
    this.provider.updateTaskList(c).then(res => {
      console.log(c.name + ' updated');
    });
  }
  deleteTaskList(c: ITaskList) {
    this.provider.deleteTaskList(c).then(res => {
      console.log(c.name + ' deleted');
      this.provider.getTaskList().then(r => {
        this.taskLists = r;
      });
    });
  }
  createTaskList() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.taskLists.push(res);
      });
    }
  }
  auth() {
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.logged = true;
        this.provider.getTaskList().then(re => {
          this.taskLists = re;
        });
      });
    }
  }
  logout() {
    this.provider.logoutt().then(res => {
      localStorage.removeItem('token');
      this.logged = false;
    });
  }
}
