import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PaginaPruebaComponent } from './pagina-prueba/pagina-prueba.component';
import { CarteraComponent } from './cartera/cartera.component';



@NgModule({
  declarations: [

    PaginaPruebaComponent,
    CarteraComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    PaginaPruebaComponent,
    CarteraComponent
  ]
})
export class PagesModule { }
