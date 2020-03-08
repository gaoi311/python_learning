(function () {
    var age = 1000;

    function f() {
        console.log(age);
        age += 1;
    }

    f();
    console.log("这老师连个JS都讲不明白！");
    f();
})();