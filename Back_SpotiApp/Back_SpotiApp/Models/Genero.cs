namespace Back_SpotiApp.Models
{
    public class Genero
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public List<Cancion> canciones { get; set; }
    }
}
