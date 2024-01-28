defmodule Solution do
  @spec two_sum(nums :: [integer], target :: integer) :: [integer]
  def two_sum(nums, target) do
    find_two_sum(nums, target)
  end

  def find_two_sum([head|tail], target, position \\\\ 0, seen \\\\ %{}) do
    if Map.has_key?(seen, target-head) do
      [Map.get(seen, target-head), position]
    else
      find_two_sum(tail, target, position+1, Map.put_new(seen, head, position))
    end
  end
end