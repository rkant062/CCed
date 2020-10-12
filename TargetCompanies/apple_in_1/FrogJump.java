class FrogJump {
    public boolean canCross(int[] stones) {
        for(int i = 3; i< stones.length; i++)
        {
            if(stones[i]>stones[i-1]*2)
                return false;
        }
        HashSet<Integer> stonehash = new HashSet<>();
        for(int i : stones)
            stonehash.add(i);
        Stack<Integer> position = new Stack<>();
        Stack<Integer> jump = new Stack<>();
        position.add(0);
        jump.add(0);
        while(!position.isEmpty())
        {
          int current_pos = position.pop();
          int jumpDistance = jump.pop();
          for(int i = jumpDistance-1; i<=jumpDistance+1; i++ )
          {
              if(i<=0)
                  continue;
              int next_pos = current_pos + i;
              if(next_pos == stones[stones.length-1])
                   return true;
              if(stonehash.contains(next_pos))
              {
                  position.add(next_pos);
                  jump.add(i);
              }
          }
        }
        return false;
    }
}