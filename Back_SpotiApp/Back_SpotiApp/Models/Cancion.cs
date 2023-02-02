namespace Back_SpotiApp.Models
{
    public class Cancion
    {
        public int Id { get; set; }
        public String Nombre { get; set; }
        public int Duracion { get; set; }
        public String autor { get; set; }
        public int GeneroId { get; set; }
        public Genero Genero { get; set; }

    }
}
