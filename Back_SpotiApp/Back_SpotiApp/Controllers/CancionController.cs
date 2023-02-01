using Back_SpotiApp.Config;
using Back_SpotiApp.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Back_SpotiApp.Controllers
{
    public class CancionController : Controller
    {
        private readonly DBSpotiContext _context;

        public CancionController(DBSpotiContext context)
        {
            _context = context;
        }

        [HttpGet("cancionlist")]
        public async Task<ActionResult<List<Cancion>>> Get()
        {
            return await _context.Canciones.ToListAsync();
        }

        [HttpPost("cancionsave")]
        public async Task<ActionResult> Post(Cancion cancion)
        {
            _context.Canciones.Add(cancion);
            await _context.SaveChangesAsync();
            return Ok(cancion);
        }
    }
}
