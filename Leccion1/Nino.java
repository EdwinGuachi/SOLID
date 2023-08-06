package P3.Leccion1;

public class Nino extends Usuario {
    public Nino(String nombre,String apellido,String cedula){
        super(nombre, apellido, cedula);
    }
    public void Jugar(){
        System.out.println("Esta jugando\n");
    }
}
