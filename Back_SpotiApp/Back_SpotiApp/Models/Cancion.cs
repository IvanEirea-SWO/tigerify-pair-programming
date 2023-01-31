namespace Back_SpotiApp.Models
{
    public class Cancion
    {
        public int Id { get; set; }
        public String Nombre { get; set; }
        public int Duracion { get; set; }
        public Album Album { get; set; }

    }
}
