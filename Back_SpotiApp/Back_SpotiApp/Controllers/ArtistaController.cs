using Back_SpotiApp.Config;
using Back_SpotiApp.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Back_SpotiApp.Controllers
{
    [Route("/api/artista")]
    public class ArtistaController : Controller
    {
        private readonly DBSpotiContext _context;

        public ArtistaController(DBSpotiContext context) 
        { 
            _context= context;
        }

        [HttpGet("list")]
        public async Task<ActionResult<List<Artista>>> Get()
        {
            return await _context.Artistas.ToListAsync();
        }

        [HttpPost("save")]
        public async Task<ActionResult> Save([FromBody] Artista artista)
        {
            if (artista == null)
            {
                return BadRequest("Los campos no pueden estar vacios");
            }
            else
            {
                _context.Artistas.Add(artista);
                await _context.SaveChangesAsync();
                return Ok(artista);
            }
        }
    }
}
