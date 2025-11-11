var MIN = 1;
var MAX = 100;

function start() {
    var randomNumber = Randomizer.nextInt(MIN, MAX);
  
        for (var i = randomNumber; i < 1000000000000; i++){
            var inputNumber = readInt("What is your guess?");
            if (randomNumber > inputNumber){
                println("Too low!");

            }else if(randomNumber < inputNumber){
                println("Too high!");

            }else if(randomNumber == inputNumber){
                println("Good job!");
                break;
            }
        }
    randomNumberGame();
       
}

function randomNumberGame(){
   var guess = readInt("Quick! Pick a number between 1-7!");
   if (guess == 4){
       println("You won the secret game :)");
   }else{
       println("You lost the secret game :(");
   }
}