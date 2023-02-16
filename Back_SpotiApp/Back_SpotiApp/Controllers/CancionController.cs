using Back_SpotiApp.Config;
using Back_SpotiApp.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Back_SpotiApp.Controllers
{
    [Route("/api/cancion")]
    public class CancionController : Controller
    {
        private readonly DBSpotiContext _context;

        public CancionController(DBSpotiContext context)
        {
            _context = context;
        }

        [HttpGet("list")]
        public async Task<ActionResult<List<Cancion>>> Get()
        {
            return await _context.Canciones.Include(x=>x.Genero).ToListAsync();
        }

        [HttpPost("save")]
        public async Task<ActionResult> Save([FromBody] Cancion cancion)
        {
            

                _context.Add(cancion);
                await _context.SaveChangesAsync();
                return Ok(cancion);

        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Cancion>> GetCancion(int id)
        {
            var cancionExist = await _context.Canciones.AnyAsync(x => x.Id == id);
            if (!cancionExist)
            {
                return BadRequest($"La cancion con id {id} no existe");
            }
            return await _context.Canciones.Include(x=>x.Genero).FirstOrDefaultAsync(x=>x.Id == id);
        }
    }
}
