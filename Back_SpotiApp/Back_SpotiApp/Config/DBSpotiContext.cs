using Back_SpotiApp.Models;
using Microsoft.EntityFrameworkCore;

namespace Back_SpotiApp.Config
{
    public class DBSpotiContext : DbContext
    {
        public DBSpotiContext(DbContextOptions<DBSpotiContext> options) : base(options)
            { }
        public DbSet<Artista> Artistas { get; set; }
        public DbSet<Album> Albums{ get; set; }
        public DbSet<Cancion> Cancion { get; set; }


    }
}

