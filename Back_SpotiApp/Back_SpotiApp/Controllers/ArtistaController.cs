using Back_SpotiApp.Config;
using Back_SpotiApp.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Back_SpotiApp.Controllers
{
    public class ArtistaController : Controller
    {
        private readonly DBSpotiContext _context;

        public ArtistaController(DBSpotiContext context) 
        { 
            _context= context;
        }

        [HttpGet("artistalist")]
        public async Task<ActionResult<List<Artista>>> Get()
        {
            return await _context.Artistas.ToListAsync();
        }

        [HttpPost("artistasave")]
        public async Task<ActionResult> Post(Artista artista)
        {
            _context.Artistas.Add(artista);
            await _context.SaveChangesAsync();
            return Ok(artista);
        }
    }
}
