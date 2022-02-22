// JavaScript Document
$(document).ready(function(e) {
    $(".middle>.cont>.class>ul>a").on("click",function(){
		$(this).addClass("net");
		$(this).siblings("a").removeClass("net");
		});
});
$(document).ready(function(e) {
    $(".middle>.cont>.class>ul>.net").on("click",function(){
		$(".all1").fadeIn();
		$(".all2,.all3,.all4,.all5,.all6,.all7,.all8,.all9,.all10").hide();
		});
});
$(document).ready(function(e) {
    $(".middle>.cont>.class>ul>._all2").on("click",function(){
		$(".all2").fadeIn();
		$(".all1,.all3,.all4,.all5,.all6,.all7,.all8,.all9,.all10").hide();
		});
});
$(document).ready(function(e) {
    $(".middle>.cont>.class>ul>._all3").on("click",function(){
		$(".all3").fadeIn();
		$(".all1,.all2,.all4,.all5,.all6,.all7,.all8,.all9,.all10").hide();
		});
});
$(document).ready(function(e) {
    $(".middle>.cont>.class>ul>._all4").on("click",function(){
		$(".all4").fadeIn();
		$(".all1,.all2,.all3,.all5,.all6,.all7,.all8,.all9,.all10").hide();
		});
});
$(document).ready(function(e) {
    $(".middle>.cont>.class>ul>._all5").on("click",function(){
		$(".all5").fadeIn();
		$(".all2,.all3,.all4,.all1,.all6,.all7,.all8,.all9,.all10").hide();
		});
});
$(document).ready(function(e) {
    $(".middle>.cont>.class>ul>._all6").on("click",function(){
		$(".all6").fadeIn();
		$(".all2,.all3,.all4,.all1,.all5,.all7,.all8,.all9,.all10").hide();
		});
});
$(document).ready(function(e) {
    $(".middle>.cont>.class>ul>._all7").on("click",function(){
		$(".all7").fadeIn();
		$(".all2,.all3,.all4,all5,.all1,.all6,.all8,.all9,.all10").hide();
		});
});
$(document).ready(function(e) {
    $(".middle>.cont>.class>ul>._all8").on("click",function(){
		$(".all8").fadeIn();
		$(".all2,.all3,.all4,all5,.all1,.all6,.all7,.all9,.all10").hide();
		});
});
$(document).ready(function(e) {
    $(".middle>.cont>.class>ul>._all9").on("click",function(){
		$(".all9").fadeIn();
		$(".all2,.all3,.all4,all5,.all1,.all6,.all7,.all8,.all10").hide();
		});
});
$(document).ready(function(e){
	$(".middle>.cont>.class>ul>._all10").on("click", function(){
		$(".all10").fadeIn();
		$(".all2,.all3,.all4,.all5,.all1,.all6,.all7,.all8,.all9").hide();
	});
});