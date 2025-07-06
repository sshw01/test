from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    avg_score = models.FloatField(default=0.0)

    def update_average_score(self):
        votes = self.vote_set.all()
        if votes.exists():
            self.avg_score = round(sum(v.score for v in votes) / votes.count(), 2)
        else:
            self.avg_score = 0.0
        self.save()

    def __str__(self):
        return self.title

class Vote(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.title} - {self.score}점"


