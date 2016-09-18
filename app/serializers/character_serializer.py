from rest_framework import serializers
from app.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('name',
                  'level',
                  'player_name',
                  'total_hp',
                  'current_hp',
                  'temporary_hp_modifier',
                  'ac',
                  'initiative',
                  'char_class',
                  'background',
                  'alignment',
                  'speed',
                  'weapons',
                  'strength',
                  'dexterity',
                  'constitution',
                  'inteligence',
                  'wisdom',
                  'charisma',
                  'presonality_trait',
                  'ideals',
                  'bonds',
                  'flaws',
                  'features',
                  'traits')
