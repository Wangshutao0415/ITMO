package attacks.status;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

public final class Moonblast extends StatusMove {
    private static final double EFFECT_CHANCE = 0.30;  // 30%几率
    public Moonblast() {
        super(Type.FAIRY, 95, 100.0);
    }

    @Override
    protected void applyOppEffects(Pokemon target) {
        // 30%几率降低特攻1级
        if (Math.random() <= EFFECT_CHANCE) {
            target.setMod(Stat.SPECIAL_ATTACK, -1);
        }
    }

    @Override
    protected String describe() {
        return "Used Moonblast";
    }
}


