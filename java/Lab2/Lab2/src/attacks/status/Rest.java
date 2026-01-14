package attacks.status;

import ru.ifmo.se.pokemon.*;

public class Rest extends StatusMove {

    public Rest() {
        super(Type.NORMAL, 0.0, 100.0);
    }

    @Override
    protected void applySelfEffects(Pokemon pokemon) {
        // 完全恢复HP - 使用setMod是最常见的方式
        double maxHP = pokemon.getStat(Stat.HP);
        double currentHP = pokemon.getHP();
        double healAmount = maxHP - currentHP;

        if (healAmount > 0) {
            // 关键：使用setMod恢复HP（负值表示恢复）
            pokemon.setMod(Stat.HP, (int) (-healAmount));
        }

        Effect sleepEffect = new Effect()
                .condition(Status.SLEEP)
                .attack(0.0)
                .turns(2);

        pokemon.setCondition(sleepEffect);
    }

    @Override
    protected String describe() {
        return "Used Rest";
    }
}