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

}
