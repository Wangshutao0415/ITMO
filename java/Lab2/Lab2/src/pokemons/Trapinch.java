package pokemons;

import attacks.status.Bulldoze;
import attacks.status.SandAttack;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Trapinch extends Pokemon {
    public Trapinch(String name, int lvl) {
        super(name, lvl);
        setStats(45, 100, 45.0, 45.0, 45.0, 10.0);
        setType(Type.GROUND);
        setMove(new Bulldoze());
        setMove(new SandAttack());
    }
}