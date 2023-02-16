using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace BackSpotiApp.Migrations
{
    /// <inheritdoc />
    public partial class context2 : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Canciones_Generos_GeneroId",
                table: "Canciones");

            migrationBuilder.AlterColumn<int>(
                name: "GeneroId",
                table: "Canciones",
                type: "int",
                nullable: true,
                oldClrType: typeof(int),
                oldType: "int");

            migrationBuilder.AddColumn<string>(
                name: "GeneroName",
                table: "Canciones",
                type: "nvarchar(max)",
                nullable: true);

            migrationBuilder.AddForeignKey(
                name: "FK_Canciones_Generos_GeneroId",
                table: "Canciones",
                column: "GeneroId",
                principalTable: "Generos",
                principalColumn: "Id");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Canciones_Generos_GeneroId",
                table: "Canciones");

            migrationBuilder.DropColumn(
                name: "GeneroName",
                table: "Canciones");

            migrationBuilder.AlterColumn<int>(
                name: "GeneroId",
                table: "Canciones",
                type: "int",
                nullable: false,
                defaultValue: 0,
                oldClrType: typeof(int),
                oldType: "int",
                oldNullable: true);

            migrationBuilder.AddForeignKey(
                name: "FK_Canciones_Generos_GeneroId",
                table: "Canciones",
                column: "GeneroId",
                principalTable: "Generos",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);
        }
    }
}
