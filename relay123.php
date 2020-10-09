<?php
    if (isset($_POST['button']))
    {
         system("gpio -g mode 21 out");
        system("gpio -g write 21 1");
    }
    else if (isset($_POST['btn']))
    {
        system("gpio -g write 21 0");
    }
?>
<html>
<body>
    <form method="post">
    <p>
        <button name="button">On Relay</button>
    </p>
    <p>
        <button name="btn">Off Relay</button>
    </p>
    </form>
</body>
</html>