using Back_SpotiApp.Models;
using Microsoft.EntityFrameworkCore;

namespace Back_SpotiApp.Config
{
    public class DBSpotiContext : DbContext
    {
        public DBSpotiContext(DbContextOptions<DBSpotiContext> options) : base(options)
            { }
        public DbSet<Cancion> Canciones { get; set; }

        public DbSet<Genero> Generos { get; set; }


    }
}

