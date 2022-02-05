class Skydiver:

    def __init__(self):

          
        cartoons = self._create_cartoon()
 
        while self._is_a_draw(cartoons):
            self._display_cartoon(cartoons)
            self._make_move(cartoons)
        
        self._display_cartoon(cartoons)
        print("You have no more parachute the game is over!")
        print() 

    def _create_cartoon(self):
        cartoon = [" ___", "/", "___", "\ ", "\ ", "/ ", "\ ", "/ ", "O", "/", "|", "\ ", "/", "\ ", "^^^^^^^"]
    
        return cartoon

    def _display_cartoon(self, cartoon):
        print()
        print(f" {cartoon[0]}")
        print(f" {cartoon[1]}{cartoon[2]}{cartoon[3]}")
        print(f" {cartoon[4]}  {cartoon[5]}")
        print(f"  {cartoon[6]}{cartoon[7]}")
        print(f"   {cartoon[8]}")
        print(f"  {cartoon[9]}{cartoon[10]}{cartoon[11]}")
        print(f"  {cartoon[12]} {cartoon[13]}")
        print()
        print(f"{cartoon[14]}")
        print()
        
    def _is_a_draw(self, cartoon):
        
        if cartoon[8] == "x" :
            return False
        return True 

        
    def _make_move(self, cartoon):
        
        puzzle = int(input("provisional entry puzzle (1-9): "))
        
        if puzzle == 1:
            cartoon[0] = "    "
        elif puzzle == 2:
            cartoon[1] = " "
        elif puzzle == 3:
            cartoon[2] = "   "
        elif puzzle == 4:
            cartoon[3] = "  "
        elif puzzle == 5:
            cartoon[4] = "  "
        elif puzzle == 6:
            cartoon[5] = "  "
        elif puzzle == 7:
            cartoon[6] = "  "
        elif puzzle == 8:
            cartoon[7] = "  "
        elif puzzle == 9:
            cartoon[8] = "x"
        else:
            pass
