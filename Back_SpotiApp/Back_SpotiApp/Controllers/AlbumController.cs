using Back_SpotiApp.Config;
using Back_SpotiApp.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Back_SpotiApp.Controllers
{
    [Route("/api/album")]
    public class AlbumController : Controller
    {
        private readonly DBSpotiContext _context;
        public AlbumController(DBSpotiContext context)
        {
            _context = context;
        }

        [HttpGet("list")]
        public async Task<ActionResult<List<Album>>> Get()
        {
            return await _context.Albums.ToListAsync();
        }

        [HttpPost("save")]
        public async Task<ActionResult> Save([FromBody] Album album)
        {
            if (album == null)
            {
                return BadRequest("Los campos no pueden estar vacios");
            }
            else
            {
                _context.Albums.Add(album);
                await _context.SaveChangesAsync();
                return Ok(album);
            }
        }

    }
}
