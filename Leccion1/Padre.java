package P3.Leccion1;

public class Padre extends Usuario {
    String lugar_trabajo;
    public Padre(String nombre,String apellido,String cedula,String lugar_trabajo){
        super(nombre, apellido, cedula);
        this.lugar_trabajo=lugar_trabajo;
    }
    public void Trabajar(){
        System.out.println("Esta trabajando\n");
    }
}
