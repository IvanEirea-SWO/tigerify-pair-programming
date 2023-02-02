using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace BackSpotiApp.Migrations
{
    /// <inheritdoc />
    public partial class @new : Migration
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

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
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

            migrationBuilder.AddForeignKey(
                name: "FK_Canciones_Generos_GeneroId",
                table: "Canciones",
                column: "GeneroId",
                principalTable: "Generos",
                principalColumn: "Id");
        }
    }
}
