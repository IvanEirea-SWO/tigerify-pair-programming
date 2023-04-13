import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-searcher',
  templateUrl: './searcher.component.html',
  styleUrls: ['./searcher.component.css']
})
export class SearcherComponent implements OnInit {

  data:any = []
  searchType:string
  searchText:string = ''

  constructor(private http:HttpClient) { // for http petitions
    this.searchType = 'songs'
    this.http.get('http://127.0.0.1:5000/song/list').subscribe(
      res => this.data = res,
      err => console.log(err)
    )
  }

  ngOnInit(): void {
  }

  onSearchTypeChange() {
    if (this.searchType === 'songs') {
      this.http.get('http://127.0.0.1:5000/song/list').subscribe(
        res => this.data = res,
        err => console.log(err)
      )
    } else if (this.searchType === 'genres') {
      this.http.get('http://127.0.0.1:5000/genre/list').subscribe(
        res => this.data = res,
        err => console.log(err)
      )
    }
  }

  onSearch() {
    if (this.searchType === 'songs') {
      this.http.get('http://127.0.0.1:5000/song/find/' + this.searchText).subscribe(
        res => this.data = res,
        err => console.log(err)
      )
    } else if (this.searchType === 'genres') {
      this.http.get('http://127.0.0.1:5000/genre/find/' + this.searchText).subscribe(
        res => this.data = res,
        err => console.log(err)
      )
    }
  }

}
