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
  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
    this.provider.getTaskList().then(res => {
      this.taskLists = res;
    });
  }
  getTask(taskList: ITaskList) {
    this.provider.getTasks(taskList).then(res => {
      // @ts-ignore
      this.tasks = res;
    });
  }
  updateTaskList(c: ITaskList) {
    this.provider.updateTask(c).then(res => {
      console.log(c.name + ' updated');
    });
  }
  deleteTaskList(c: ITaskList) {
    this.provider.deleteTask(c.id).then(res => {
      console.log(c.name + ' deleted');
      this.provider.getTaskList().then(r => {
        this.taskLists = r;
      });
    });
  }
  createTaskList() {
    if (this.name !== '') {
      this.provider.createTask(this.name).then(res => {
        this.name = '';
        this.taskLists.push(res);
      });
    }
  }
}
