package pokemons;

import attacks.status.Growth;
import attacks.status.Rest;
import attacks.status.RockTomb;
import attacks.status.Swagger;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Flygon extends Vibrava {
    public Flygon(String name, int lvl) {
        super(name, lvl);
        setStats(80, 100, 80, 80, 80, 100);
        setType(Type.GROUND, Type.DRAGON);
        setMove(new RockTomb());
    }
}
