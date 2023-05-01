import { NgModule } from '@angular/core';
import { CommonModule, registerLocaleData } from '@angular/common';
import { PaginaPruebaComponent } from './pagina-prueba/pagina-prueba.component';
import { CarteraComponent } from './cartera/cartera.component';
import { PerfilUsuarioComponent } from './perfil-usuario/perfil-usuario.component';
import { RegistroComponent } from './registro/registro.component';
import { AppRoutingModule } from '../app-routing.module';



@NgModule({
  declarations: [

    PaginaPruebaComponent,
    CarteraComponent,
    PerfilUsuarioComponent,
    RegistroComponent
  ],
  imports: [
    CommonModule,
    AppRoutingModule
  ],
  exports: [
    PaginaPruebaComponent,
    CarteraComponent,
    PerfilUsuarioComponent,
    RegistroComponent
  ]
})
export class PagesModule { }
