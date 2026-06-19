class LetterView(discord.ui.View):
    def __init__(self, letter_text):
        super().__init__(timeout=None)
        self.letter_text = letter_text

    @discord.ui.button(label="open letter!", style=discord.ButtonStyle.primary)
    async def open_letter(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            self.letter_text,
            ephemeral=True
        )
