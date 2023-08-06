package P3.Leccion1;

public class Usuario{
    String nombre;
    String apellido;
    String cedula;

    public Usuario(String nombre,String apellido,String cedula){
        this.nombre=nombre;
        this.apellido=apellido;
        this.cedula=cedula;
    }
    public void Correr(){
        System.out.println("Esta corriendo\n");
    }
    public void Saltar(){
        System.out.println("Salta\n");
    }
}