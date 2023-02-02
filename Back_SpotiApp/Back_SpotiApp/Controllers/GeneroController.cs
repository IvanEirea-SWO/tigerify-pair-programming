using Back_SpotiApp.Config;
using Back_SpotiApp.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Back_SpotiApp.Controllers
{
    public class GeneroController : Controller
    {
        private readonly DBSpotiContext _context;

        public GeneroController(DBSpotiContext context)
        {
            _context = context;
        }

        [HttpGet("generolist")]
        public async Task<ActionResult<List<Genero>>> Get()
        {
            return await _context.Generos.ToListAsync();
        }

        [HttpPost("generosave")]
        public async Task<ActionResult> Post(Genero genero)
        {
            _context.Generos.Add(genero);
            await _context.SaveChangesAsync();
            return Ok(genero);
        }
    }
}

