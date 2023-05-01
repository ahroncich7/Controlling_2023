import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CarteraComponent } from './pages/cartera/cartera.component';
import { PerfilUsuarioComponent } from './pages/perfil-usuario/perfil-usuario.component';
import { RegistroComponent } from './pages/registro/registro.component';

const routes: Routes = [

  {path: "cartera", component: CarteraComponent},
  {path: "perfil_usuario", component: PerfilUsuarioComponent},
  {path: "registro", component: RegistroComponent}


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
