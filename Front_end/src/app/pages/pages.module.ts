import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PaginaPruebaComponent } from './pagina-prueba/pagina-prueba.component';



@NgModule({
  declarations: [
  
    PaginaPruebaComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    PaginaPruebaComponent
  ]
})
export class PagesModule { }
