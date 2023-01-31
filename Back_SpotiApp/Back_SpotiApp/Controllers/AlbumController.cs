using Back_SpotiApp.Config;
using Back_SpotiApp.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Back_SpotiApp.Controllers
{
    public class AlbumController : Controller
    {
        private readonly DBSpotiContext _context;
        public AlbumController(DBSpotiContext context)
        {
            _context = context;
        }

        [HttpGet("albumlist")]
        public async Task<ActionResult<List<Album>>> Get()
        {
            return await _context.Albums.ToListAsync();
        }

        [HttpPost("albumsave")]
        public async Task<ActionResult> Post(Album album) 
        {
            _context.Albums.Add(album);
            await _context.SaveChangesAsync();
            return Ok(album);
        }

    }
}
