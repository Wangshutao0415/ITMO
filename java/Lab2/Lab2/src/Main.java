import pokemons.Cottonee;
import pokemons.Whimsicott;
import ru.ifmo.se.pokemon.Battle;
import ru.ifmo.se.pokemon.Pokemon;
import pokemons.*;

public class Main {
    public static void main(String[] args) {
        Battle b = new Battle();
        Pokemon p1 = new Basculin("Basculin", 41);
        Pokemon p2 = new Cottonee("Cottonee", 44);
        Pokemon p3 = new Whimsicott("Whimsicott", 50);
        Pokemon p4 = new Trapinch("Trapinch", 9);
        Pokemon p5 = new Vibrava("Vibrava", 47);
        Pokemon p6 = new Flygon("Flygon", 39);
        b.addAlly(p1);
        b.addAlly(p2);
        b.addAlly(p3);
        b.addFoe(p4);
        b.addFoe(p5);
        b.addFoe(p6);
        b.go();
    }
}