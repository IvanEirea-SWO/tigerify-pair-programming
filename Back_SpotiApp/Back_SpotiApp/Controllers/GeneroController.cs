using Back_SpotiApp.Config;
using Back_SpotiApp.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Back_SpotiApp.Controllers
{
    [Route("/api/genero")]
    public class GeneroController : Controller
    {
        private readonly DBSpotiContext _context;

        public GeneroController(DBSpotiContext context)
        {
            _context = context;
        }

        [HttpGet("list")]
        public async Task<ActionResult<List<Genero>>> Get()
        {
            return await _context.Generos.ToListAsync();
        }

        [HttpPost("save")]
        public async Task<ActionResult> Save([FromBody] Genero genero)
        {
            if (genero == null)
            {
                return BadRequest("Los campos no pueden estar vacios");
            }
            else
            {
                _context.Generos.Add(genero);
                await _context.SaveChangesAsync();
                return Ok(genero);
            }
        }
        [HttpGet("buscar-id/{id}")]
        public async Task<ActionResult<Genero>> GetGenero(int id)
        {
            var generoExist = await _context.Generos.AnyAsync(x => x.Id == id);
            if (!generoExist)
            {
                return BadRequest($"La cancion con id {id} no existe");
            }
            return await _context.Generos.Include(x => x.canciones).FirstOrDefaultAsync(x => x.Id == id);
        }

        [HttpGet("buscar-nombre/{name}")]
        public async Task<ActionResult<Genero>> GetGenero(String name)
        {
            var generoExist = await _context.Generos.AnyAsync(x => x.Name == name);
            if (!generoExist)
            {
                return BadRequest($"La cancion con nombre {name} no existe");
            }
            return await _context.Generos.Include(x => x.canciones).FirstOrDefaultAsync(x => x.Name == name);
        }

        [HttpPut("/update/{id}")]
        public async Task<ActionResult> Put(int id, Genero genero)
        {
            _context.Entry(genero).State = EntityState.Modified;
            await _context.SaveChangesAsync();
            return Ok(genero);
        }

        [HttpDelete("/delete/{id}")]
        public async Task<ActionResult> Delete(int id)
        {
            var genero = await _context.Generos.FindAsync(id);
            _context.Remove(genero);
            await _context.SaveChangesAsync();
            return NoContent();
        }
    }
}

