

procedure main() do
    $a = 1
    $b = 1
    print("0")
    during True do
        $c = $a + $b
        print($c)
        $b = $a
        $a = $c
    end
end

