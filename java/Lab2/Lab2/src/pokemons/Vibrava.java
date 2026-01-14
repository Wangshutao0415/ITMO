package pokemons;

import attacks.status.Bulldoze;
import attacks.special.Boomburst;
import attacks.status.SandAttack;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Vibrava extends Pokemon {
    public Vibrava(String name, int lvl) {
        super(name, lvl);
        setStats(50.0, 70.0, 50.0, 50.0, 50.0, 70.0);
        setType(Type.GROUND,Type.DRAGON);
        setMove(new Bulldoze());
        setMove(new SandAttack());
        setMove(new Boomburst());
    }
}
