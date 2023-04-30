import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PaginaPruebaComponent } from './pagina-prueba/pagina-prueba.component';
import { CarteraComponent } from './cartera/cartera.component';
import { PerfilUsuarioComponent } from './perfil-usuario/perfil-usuario.component';



@NgModule({
  declarations: [

    PaginaPruebaComponent,
    CarteraComponent,
    PerfilUsuarioComponent
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
