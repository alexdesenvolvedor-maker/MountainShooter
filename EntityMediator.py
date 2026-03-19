from EnemyShot import EnemyShot
from PlayerShot import PlayerShot
from Const import WIN_WIDTH
from Enemy import Enemy
from Entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i  in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

        # chama o método privado corretamente
        EntityMediator.__verify_health(entity_list)

    @staticmethod
    def __verify_health(entity_list: list[Entity]):
        entity_list[:] = [ent for ent in entity_list if ent.health > 0]