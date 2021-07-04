import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AgGridAngular } from 'ag-grid-angular';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'UI';
  private gridApi: any;

  columnDefs = [
    { field: 'sl', sortable: true, filter: true, checkboxSelection: true },
    { field: 'name', sortable: true, filter: true },
    { field: 'email', sortable: true, filter: true }
  ];
  rowData: Observable<any[]> | undefined;


  constructor(private http: HttpClient) {
  }

  ngOnInit(): void {
    this.load();
  }
  load():void {
    this.http.get<any[]>('http://localhost:8007/list').subscribe((data: any) => {
      console.log(data, JSON.parse(data.data));
      this.rowData = JSON.parse(data.data);

    });
  }

  onBtnExport(): void {
    this.gridApi.exportDataAsCsv();
  }
  onGridReady(params: any) {
    this.gridApi = params.api;
    // this.gridColumnApi = params.columnApi;
  }
  save() {
    let name: any = document.getElementById('name');
    let email: any = document.getElementById('email');
    if (name.value && email.value) {
      let d: any = { name: name.value, email: email.value };
      console.log('d', d);
      this.http.post<any[]>("http://localhost:8007/save", d).subscribe((data) => {
        console.log("result", data);
        let el: any = document.getElementById('new-form');
        el.reset();
        this.load();
      });
    }
  }
}
